def test_events(page):
    def print_request_sent(request):
        print("Request sent: " + request.url)

    def print_request_finished(request):
        print("Request finished: " + request.url)

    page.on("request", print_request_sent)
    page.on("requestfinished", print_request_finished)
    page.goto("https://wikipedia.org")

    page.remove_listener("requestfinished", print_request_finished)
    page.goto("https://www.openstreetmap.org/")