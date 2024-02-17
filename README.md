# GeminiDiscordBot

Create an AI Discord bot with Google's Gemini Pro for **free**.

## Steps

1. **Clone this repository:**

    ```sh
    git clone https://github.com/pranavpudasaini/GeminiDiscordBot && cd GeminiDiscordBot
    ```

2. **[Generate Discord Bot API token](https://discordpy.readthedocs.io/en/stable/discord.html)**

3. **[Generate Gemini API key](https://aistudio.google.com/)**

4. **Build docker image:**

    ```sh
    docker build . -t gemini:v1
    ```

5. **Copy `.env.example` to `.env` and populate API keys:**

    ```sh
    cp .env.example .env
    ```

6. **Run docker container with the environment variable file:**

    ```sh
    docker run --rm gemini:v1
    ```

