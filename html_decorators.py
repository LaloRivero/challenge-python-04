def div(func):
    # You have to code here!
    def wrapper(nombre):
        return f'<div> ¡Hola {nombre}, ¿Cómo estás? </div>'

    return wrapper


def article(func):
    # You have to code here!
    def wrapper(nombre):
        return f'<article> ¡Hola {nombre}, ¿Cómo estás? </article>'

    return wrapper


def p(func):
    # You have to code here!
    def wrapper(nombre):
        return f'<p> ¡Hola {nombre}, ¿Cómo estás? </p>'

    return wrapper


# Here you must apply the decorators, uncomment this later
# @div
# @article
@p
def saludo(nombre):
    return f'¡Hola {nombre}, ¿Cómo estás?'


def run():
    print(saludo('Jorge'))


if __name__ == '__main__':
    run()

# We want to have three different outputs 👇🏼

# <div>¡Hola Jorge, ¿Cómo estás?'</div>
# <article>¡Hola Jorge, ¿Cómo estás?'</article>
# <p>¡Hola Jorge, ¿Cómo estás?'</p>
