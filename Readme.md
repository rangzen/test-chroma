# Getting Started of Chroma

Small tests on [Chroma](https://www.trychroma.com).

## Requirements

```
pip install --user pipenv
pipenv --python 3
pipenv shell
pip install chromadb
```

## Embeddings

Update `source_relative_path` to point to a directory containing Markdown files.

To create the persistent collection locally, run [getting-started-create.py](./getting-started-create.py).

## Query

Modify `query_texts` to the desired prompt.

To see the query result on the parsed documents, run [getting-started-query.py](./getting-started-query.py).

### Additional Resources

For more information on Chroma, you can refer to the following resources:

- [Chroma Documentation](https://docs.trychroma.com): This is the official documentation for Chroma, which provides detailed information on its features, usage, and configuration.

- [Chroma GitHub Repository](https://github.com/chroma-core/chroma): The Chroma GitHub repository contains the source code, issue tracker, and community discussions related to Chroma. You can explore the repository to gain a deeper understanding of Chroma's implementation and contribute to its development.

Feel free to explore these resources to enhance your knowledge of Chroma and make the most out of its capabilities.
