from http.server import HTTPServer, SimpleHTTPRequestHandler

# Remember to do latexmk -pdf -pvc main.tex

HOST = "0.0.0.0"
PORT = 8000

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print(f"PDF: http://localhost:{PORT}/main.pdf")
print("Press Ctrl+C to stop.")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
    server.server_close()
