{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "loda_data",
      "provenance": [],
      "authorship_tag": "ABX9TyMD6LhN1n4sAVYnmlB1G//b",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sda96/AIFFEL_3rd_hackerton_TUNiB_DKTC/blob/main/notebook/SeHyun/Custom%20Libraries/loda_data.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "4rSVxZWMRZXx"
      },
      "outputs": [],
      "source": [
        "import os\n",
        "from io import open\n",
        "\n",
        "import torch\n",
        "\n",
        "import nltk\n",
        "\n",
        "# Custom libraries\n",
        "from preprocess import DataPreprocessor"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class Dictionary(object):\n",
        "    \"\"\"\n",
        "    Creates a dictionary with tokens mapped to their positional ids and vice-versa.\n",
        "    \"\"\"\n",
        "    def __init__(self):\n",
        "        self.word2idx = {}\n",
        "        self.idx2word = []\n",
        "\n",
        "    def add_word(self, word):\n",
        "        if word.lower() not in self.word2idx:\n",
        "            self.idx2word.append(word.lower())\n",
        "            self.word2idx[word.lower()] = len(self.idx2word) - 1\n",
        "        return self.word2idx[word.lower()]\n",
        "\n",
        "    def __len__(self):\n",
        "        return len(self.idx2word)\n",
        "\n",
        "\n",
        "class Corpus(object):\n",
        "    def __init__(self, path):\n",
        "        self.dictionary = Dictionary()\n",
        "        self.train = self.tokenize(os.path.join(path, 'wikitext-2-raw-v1', 'wiki.train.raw'))\n",
        "        self.valid = self.tokenize(os.path.join(path, 'wikitext-2-raw-v1', 'wiki.valid.raw'))\n",
        "        self.test = self.tokenize(os.path.join(path, 'wikitext-2-raw-v1', 'wiki.test.raw'))\n",
        "\n",
        "    def tokenize(self, path):\n",
        "        \"\"\"\n",
        "        Takes the train, valid, and test files from the unsup corpus and tokenizes them to form a LongTensors of ids.\n",
        "        \"\"\"\n",
        "        # Add words to the dictionary\n",
        "        with open(path, 'r', encoding=\"utf8\") as f:\n",
        "            tokens = 0\n",
        "            for line in f:\n",
        "                sent_text = nltk.sent_tokenize(line) # this gives us a list of sentences\n",
        "                tokenized_text = []\n",
        "                for sentence in sent_text:\n",
        "                    current_sent = nltk.word_tokenize(sentence)\n",
        "                    current_sent.insert(len(current_sent), \"eos\")\n",
        "                    tokenized_text.append(current_sent)\n",
        "                text = [item for sublist in tokenized_text for item in sublist]\n",
        "                words = text + ['eop']\n",
        "                tokens += len(words)\n",
        "                for word in words:\n",
        "                    self.dictionary.add_word(word.lower())\n",
        "\n",
        "        # Tokenize file content\n",
        "        with open(path, 'r', encoding=\"utf8\") as f:\n",
        "            ids = torch.LongTensor(tokens)\n",
        "            token = 0\n",
        "            for line in f:\n",
        "                sent_text = nltk.sent_tokenize(line) # this gives us a list of sentences\n",
        "                tokenized_text = []\n",
        "                for sentence in sent_text:\n",
        "                    current_sent = nltk.word_tokenize(sentence)\n",
        "                    current_sent.insert(len(current_sent), \"eos\")\n",
        "                    tokenized_text.append(current_sent)\n",
        "                text = [item for sublist in tokenized_text for item in sublist]\n",
        "                words = text + ['eop']\n",
        "                for word in words:\n",
        "                    ids[token] = self.dictionary.word2idx[word.lower()]\n",
        "                    token += 1\n",
        "        return ids"
      ],
      "metadata": {
        "id": "7TGFlSMVRrCD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "MBgRZnCqRrHQ"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}