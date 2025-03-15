from livereload import Server, shell

server = Server()

# Watch the main HTML, CSS, and JS files, and the images directory
server.watch('index.html', shell('echo "index.html changed"'))
server.watch('style.css', shell('echo "style.css changed"'))
server.watch('projects.html', shell('echo "projects.html changed"'))
server.watch('photography.html', shell('echo "photography.html changed"'))
# server.watch('hobbies.html', shell('echo "hobbies.html changed"')) # Not in chat
server.watch('images/', shell('echo "images changed"'))

# Serve the current directory
server.serve(root='.', port=8000, open_url_delay=0)
