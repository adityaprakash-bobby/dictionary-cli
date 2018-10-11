import click
import requests
import json

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()

def define (word_id):
    """
    Function to fetch the definition from the OXFORD dictionary API
    """
    app_id = '03d6694b'
    app_key = '7ebdd9bf9b5015c27868ed543de2f28a'
    language = 'en'

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

    data = json.loads(r.content)
    definition = data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]

    return definition


# The application section
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('-w', '--word',
                help='Enter a word')
@click.option('--version', is_flag=True, callback=print_version,
                expose_value=False, is_eager=True)

def cli(word):
    """
    This app lets you find meaning of words in the CLI itself. How cool!
    """
    try :
        click.echo(click.style(word , fg='red', bold=True))
        click.echo(click.style("\t" + str(define(word)), fg = 'green'))
    except ValueError :
        click.echo('Error : Not a valid word!')
    except TypeError :
        click.echo("Error : No parameters passed!")
