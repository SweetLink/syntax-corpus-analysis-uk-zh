import matplotlib.pyplot as plt

def create_graph(corpus_data):
  """
  Creates a graph with dots representing sentence, composite sentence, and subordinate clause counts for each text in the corpus.

  Args:
      corpus_data (list): A list of dictionaries, where each dictionary represents a text with the following keys:
          - 'text': The original text string.
          - 'total_sentences': The total number of sentences in the text.
          - 'composite_sentences': The number of composite sentences in the text.
          - 'subordinate_clauses': The total number of subordinate clauses in the text.
  """

  text_labels = [text['text'] for text in corpus_data]  # Extract text labels for x-axis
  sentence_counts = [text['total_sentences'] for text in corpus_data]
  composite_counts = [text['composite_sentences'] for text in corpus_data]
  subordinate_counts = [text['subordinate_clauses'] for text in corpus_data]

  # Create the plot with three lines (one for each metric) using different colors and markers
  plt.plot(text_labels, sentence_counts, 'bo-', label='Total Sentences')
  plt.plot(text_labels, composite_counts, 'gs-', label='Composite Sentences')
  plt.plot(text_labels, subordinate_counts, 'ro-', label='Subordinate Clauses')

  # Customize the plot for clarity and aesthetics
  plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for readability
  plt.xlabel('Texts in Corpus')
  plt.ylabel('Number of Sentences/Clauses')
  plt.title('Sentence and Clause Breakdown by Text')
  plt.subplots_adjust(bottom=0.2)  # Adjust plot layout for better label visibility
  plt.legend()  # Add legend for clarity

  plt.tight_layout()  # Improve spacing between elements
  plt.show()

# Example usage (replace with your actual corpus data)
corpus_data = [
  {'text': "This is a simple sentence.", 'total_sentences': 1, 'composite_sentences': 0, 'subordinate_clauses': 0},
  {'text': "This is a compound sentence with two independent clauses.", 'total_sentences': 2, 'composite_sentences': 1, 'subordinate_clauses': 0},
  {'text': "This sentence has a dependent clause, which makes it a complex sentence.", 'total_sentences': 1, 'composite_sentences': 1, 'subordinate_clauses': 1},
]

create_graph(corpus_data)
