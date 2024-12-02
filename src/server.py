# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer
import os


# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


file_path = os.path.join(os.path.abspath("../contacts.html"))
css_directory = os.path.join(os.path.abspath("../css"))


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""
        if self.path.endswith(".css"):
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()

            css_file_path = os.path.join(css_directory, "bootstrap.min.css")
            try:
                with open(css_file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    self.wfile.write(bytes(content, "utf-8"))
            except IOError:
                self.send_error(404, "File Not Found: %s" % self.path)

        elif self.path == "/":
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    self.send_response(200)  # Отправка кода ответа
                    self.send_header(
                        "Content-type", "text/html"
                    )  # Отправка типа данных
                    self.end_headers()  # Завершение формирования заголовков ответа
                    self.wfile.write(bytes(content, "utf-8"))  # Тело ответа
            except IOError:
                self.send_error(404, "File Not Found: %s" % self.path)
        else:
            self.send_error(404, "File Not Found: %s" % self.path)


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрах в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
