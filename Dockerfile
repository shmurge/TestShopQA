FROM python:3.11-bookworm

# Java and Firefox
RUN apt-get update && apt-get install -y \
    wget gnupg ca-certificates firefox-esr default-jdk

# Chrome
RUN mkdir -p /etc/apt/keyrings \
    && wget -qO /etc/apt/keyrings/google.asc https://dl.google.com/linux/linux_signing_key.pub \
    && echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/google.asc] https://dl.google.com/linux/chrome/deb/ stable main" \
       > /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable

# Allure
RUN wget https://github.com/allure-framework/allure2/releases/download/2.32.0/allure-2.32.0.tgz \
    && tar -zxvf allure-2.32.0.tgz -C /opt/ \
    && ln -sf /opt/allure-2.32.0/bin/allure /usr/bin/allure

WORKDIR /usr/workspace
COPY requirements.txt .
RUN pip install -r requirements.txt