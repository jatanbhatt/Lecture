#!/usr/bin/env python

# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This application demonstrates label detection,
explicit content, and shot change detection using the Google Cloud API.
Usage Examples:
    python analyze.py labels gs://cloud-ml-sandbox/video/chicago.mp4
    python analyze.py labels_file resources/cat.mp4
    python analyze.py shots gs://demomaker/gbikes_dinosaur.mp4
    python analyze.py explicit_content gs://demomaker/gbikes_dinosaur.mp4
"""

import argparse
import io

from google.cloud import videointelligence
from google.cloud.videointelligence import enums


def speech_transcription(path):
    # [START video_speech_transcription_gcs]
    """Transcribe speech from a video stored on GCS."""
    from google.cloud import videointelligence

    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.SPEECH_TRANSCRIPTION]

    config = videointelligence.types.SpeechTranscriptionConfig(
        language_code='en-US',
        enable_automatic_punctuation=True)
    video_context = videointelligence.types.VideoContext(
        speech_transcription_config=config)

    operation = video_client.annotate_video(
        path, features=features,
        video_context=video_context)

    print('\nProcessing video for speech transcription.')

    result = operation.result(timeout=600)

    # There is only one annotation_result since only
    # one video is processed.
    annotation_results = result.annotation_results[0]
    for speech_transcription in annotation_results.speech_transcriptions:

        # The number of alternatives for each transcription is limited by
        # SpeechTranscriptionConfig.max_alternatives.
        # Each alternative is a different possible transcription
        # and has its own confidence score.
        for alternative in speech_transcription.alternatives:
            print('Alternative level information:')

            print('Transcript: {}'.format(alternative.transcript))
            print('Confidence: {}\n'.format(alternative.confidence))

            print('Word level information:')
            for word_info in alternative.words:
                word = word_info.word
                start_time = word_info.start_time
                end_time = word_info.end_time
                print('\t{}s - {}s: {}'.format(
                    start_time.seconds + start_time.nanos * 1e-9,
                    end_time.seconds + end_time.nanos * 1e-9,
                    word))
    # [END video_speech_transcription_gcs]


speech_transcription("gs://lecturetest/Voltage.mp4")