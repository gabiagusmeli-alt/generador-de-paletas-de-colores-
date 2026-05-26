import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
threads = 2
bind = "0.0.0.0:8000"
timeout = 30
accesslog = "-"
errorlog = "-"
loglevel = "info"
secure_scheme_headers = {"X-FORWARDED-PROTO": "https"}
