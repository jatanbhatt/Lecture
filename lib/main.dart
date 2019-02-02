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

class RandomWordsState extends State<RandomWords> {
    final _suggestions = <WordPair>[];
    final _biggerFont = const TextStyle(fontSize: 18.0);
    @override
    Widget _buildSuggestions() {
        return ListView.builder(
            padding: const EdgeInset.all(16:0),
            itemBuilder: (context, i) {
                if (i.is0dd) return Divider();
                final index = i ~/ 2;
                if (index >= _suggestions.length) {
                    _suggestions.addAll(generateWordPairs().take(10)); /*4*/
                }
                return _buildRow(_suggestions[index]);
            }
        );
    }
    @override
    Widget _buildRow(WordPair pair) {
        return ListTile(
            title: Text(
                pair.asPascalCase,
                style: _biggerFont,
            ),
        );
    }
}
