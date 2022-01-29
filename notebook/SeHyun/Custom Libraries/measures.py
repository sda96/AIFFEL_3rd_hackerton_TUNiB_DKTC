{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "measures.py",
      "provenance": [],
      "authorship_tag": "ABX9TyMxvyDDpJUmJTqQX5lKmfZj",
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
        "<a href=\"https://colab.research.google.com/github/sda96/AIFFEL_3rd_hackerton_TUNiB_DKTC/blob/main/notebook/SeHyun/Custom%20Libraries/measures.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "aAvzZktrNep5"
      },
      "outputs": [],
      "source": [
        "#import libraries\n",
        "import pickle\n",
        "\n",
        "import numpy as np"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "_SQRT2 = np.sqrt(2)     # sqrt(2) with default precision np.float64\n",
        "def hellinger_distance(p, q):\n",
        "    \"\"\"\n",
        "    Calculates the hellinger distance for two different probability distribution.\n",
        "    :param p,q: a dictionary with its keys being unique tokens and value being their max-activations(dtype:dict) \n",
        "    :return: average hellinger distance and total number of features activated for a particular neuron\n",
        "    \"\"\"\n",
        "    all_unique_tokens = set(p.keys()) | set(q.keys())\n",
        "    \n",
        "    # Adding tokens from all_unique_tokens to the dictionaries p and q\n",
        "    for token in all_unique_tokens:\n",
        "        if token not in p:\n",
        "            p[token] = 0\n",
        "        if token not in q:\n",
        "            q[token] = 0\n",
        "    \n",
        "    # preparing the sorted dictionaries\n",
        "    a, b = ({} for i in range(2))\n",
        "    sorted_keys = sorted(p.keys())\n",
        "    for token in sorted_keys:\n",
        "        a[token] = p[token]\n",
        "        b[token] = q[token]\n",
        "    \n",
        "    hellinger_distance = np.sqrt(np.sum((np.sqrt(list(a.values())) - np.sqrt(list(b.values()))) ** 2)) / _SQRT2\n",
        "    return hellinger_distance/len(a), len(a)\n",
        "\n",
        "def find_shared_neurons(listA, listB):\n",
        "    \"\"\"\n",
        "    :param listA: list of unique neurons in A(dtype:list of int)\n",
        "    :param listA: list of unique neurons in B(dtype:list of int)\n",
        "    :return: shared neurons between list A and B(dtype:list of int)\n",
        "    \"\"\"\n",
        "    shared_neurons = set.intersection(set(listA), set(listB))\n",
        "    return list(shared_neurons)\n",
        "\n",
        "def calculate_hellinger_distance(model1, model2, filename):\n",
        "    \"\"\"\n",
        "    :param model1:data from trained model 1\n",
        "    :param model2:data from trained model 2\n",
        "    :param filename: pickled file name and directory to store the results\n",
        "    \"\"\"\n",
        "    hellinger_dict = {}\n",
        "\n",
        "    # Finding shared neurons between the two models\n",
        "    model1_neurons = list(model1['max_activation_index'].unique())\n",
        "    model2_neurons = list(model2['max_activation_index'].unique())\n",
        "    shared_neurons = find_shared_neurons(model1_neurons, model2_neurons)\n",
        "\n",
        "    for neuron in shared_neurons:\n",
        "        # Loading the data for both the models\n",
        "        model1_data = model1[model1['max_activation_index'] == neuron]\n",
        "        model1_data[\"normalized_max_activations\"] = model1_data[\"max_activations\"].apply(lambda x: x/model1_data[\"max_activations\"].sum())\n",
        "        model2_data = model2[model2['max_activation_index'] == neuron]\n",
        "        model2_data[\"normalized_max_activations\"] = model2_data[\"max_activations\"].apply(lambda x: x/model2_data[\"max_activations\"].sum())\n",
        "        \n",
        "        # Getting all the unique tokens from both the models so the average can be taken.\n",
        "        model1_dict, model2_dict = ({} for i in range(2))\n",
        "        unique_tokens_model1 = model1_data['inputs'].unique()\n",
        "        unique_tokens_model2 = model2_data['inputs'].unique()\n",
        "        \n",
        "        for token in unique_tokens_model1:\n",
        "            temp = model1_data[model1_data['inputs'] == token]\n",
        "            model1_dict[token] = temp['normalized_max_activations'].mean()\n",
        "        \n",
        "        for token in unique_tokens_model2:\n",
        "            temp = model2_data[model2_data['inputs'] == token]\n",
        "            model2_dict[token] = temp['normalized_max_activations'].mean()\n",
        "        \n",
        "        distance, num_tokens = hellinger_distance(model1_dict,model2_dict)\n",
        "        # Hellinger Dictionary contains the distance between two model for a given activation and total number of\n",
        "        # tokens compared between these two models.\n",
        "        hellinger_dict[neuron] = (distance, num_tokens)\n",
        "\n",
        "        # Dumping the dictionary\n",
        "        with open(filename, 'wb') as handle:\n",
        "            pickle.dump(hellinger_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)\n"
      ],
      "metadata": {
        "id": "RHgVsYzmNpYv"
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
        "id": "BL4O1G1WNpdG"
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
        "id": "QxPkEXyZNpiU"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}