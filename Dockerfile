FROM khalosa/rasa-aarch64:3.5.2

WORKDIR /app

COPY ./chatbot/actions/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./chatbot/actions /app/actions

ENTRYPOINT ["rasa"]

CMD ["run", "actions"]
