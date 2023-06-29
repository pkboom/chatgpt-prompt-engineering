# Start a new environment

```sh
conda create -n openai -c conda-forge ipykernel panel python-dotenv openai jupyter_bokeh
```

# Remove an environment

```sh
conda remove -n openai --all
```

# Activate/Deactivate an environment

```sh
conda activate openai

conda deactivate
```

# API keys

[Open ai API keys](https://platform.openai.com/account/api-keys)

Set `OPENAI_API_KEY` in `.env`.

# A note about the backslash

- In the course, we are using a backslash `\` to make the text fit on the screen without inserting newline '\n' characters.
- GPT-3 isn't really affected whether you insert newline characters or not. But when working with LLMs in general, you may consider whether newline characters in your prompt may affect the model's performance.
