import 'package:flutter/material.dart';
import 'package:english_words/english_words.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final wordPair = WordPair.random();
    return MaterialApp(
      title: 'Welcome to Flutter',
      home: Scaffold(
        appBar: AppBar(
          title: Text('Homepage'),
        ),
        body: Center(
          child: Text(wordPair.asPascalCase), // Pascal case -> every word in string starts with cap
        ),
      ),
    );
  }
}
