# cyprus-bot

Это бот на английском языке, отвечающий на вопросы про релокацию на Кипр.

С ним можно пообщаться тут: https://t.me/cyprus_relocate_bot.

***

Бот написан на фреймворке Rasa Open Source.
Для всех интентов я прописала обучающие фразы, поэтому общаться с ботом можно как кнопками, так и текстом.

Также я добавила генерацию ответов на основе вики. Для этого я запустила локально квантованную версию Llama3 и отправляю в неё только запросы, классифицированные в соответствующий интент.

Я провела ручное тестирование работы бота, критичных ошибок не обнаружила.

***
**Rasa Open Source**

С этим фреймворком я хорошо знакома, поэтому проще всего мне было использовать именно его. Rasa обеспечивает легкость в масштабировании и очень гибко настраивается. Её удобно использовать как для небольших ботов, так и для сложных проектов с разветвленными сценариями и интеграциями.
Я сделала бота на английском, но представляю, как параллельно запустить модель и для русского языка тоже.

**Docker**

Обеспечивает воспроизводимость среды разработки, может использоваться для дальнейшего развертывания на сервере.

**ngrok**

Для связи Telegram и бота я настроила ngrok, потому что это простой и безопасный инструмент для предоставления доступа к локальному серверу.

**LM Studio**

Эта платформа помогает демонстрировать работу различных моделей. Я запустила модель локально, что обеспечивает полный контроль над данными и их безопасность. Взаимодействие с ней очень похоже на взаимодействие с ChatGPT API, и не зависит от выбранной модели, что упрощает подбор оптимальной версии.
