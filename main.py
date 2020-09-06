from app import Application


def main():

    # TODO: Read config from JSON file
    config = {
        'info': {
            'title': 'The Black Box',
            'logo': 'logo.png',
            'author': 'Rich Saupe',
            'version': .1,
            'description': 'The Black Box is a mystery.  Interigate it using different inputs to see if you can figure out its purpose.',
            'python_version': '3.7+'
        },
        'font': {
            'name': 'Arial',
            'font_size': 60
        },
        'display': {
            'fps': 30
        }
    }

    app = Application(config)
    app.run()


if __name__ == "__main__" :
    main()
