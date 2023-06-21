# Mini Django

This is a minimal Django project that serves a single "Hello World" response at the root URL, contained entirely within a single Python script. It's intended as a simple example of how to set up a basic Django project using only the core Django modules and functions in a single file.

## Requirements

To run this project, you'll need:

- Python 3.6 or higher
- Django 2.2 or higher

## Usage

To run the project, simply clone the repository and run the following command:

```bash
python main.py runserver
```

This will start the development server at (localhost:8000)[http://localhost:8000/]. You should see a "Hello World" message when you visit that URL in your web browser.

## Features
This project is unique in that it contains the entire Django project within a single Python script. This approach has several advantages, including:

- **Simplicity**: By containing everything in a single file, the project is much simpler and easier to understand than a full-fledged Django project with multiple files and directories.
- **Portability**: Since the project is self-contained, it can be easily shared or moved between different environments without having to worry about file paths or dependencies.
- **Experimentation**: The single-file approach makes it easy to experiment with Django features or test out new ideas without having to create a full project each time.

However, it's worth noting that this approach has some limitations as well. For example, it may not be suitable for larger or more complex projects, and it may not take advantage of Django's full capabilities. Additionally, it may be more difficult to maintain or modify the project over time as it grows in complexity.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
