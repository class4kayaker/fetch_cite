import click
import fetch_cite.fetcher


@click.command()
@click.argument('dois', nargs=-1)
def get_cite(dois):
    """
    Fetch citations for DOIs in [bibtex] format
    """
    code = fetch_cite.fetcher.get_format_code('bibtex')
    for doi in dois:
        try:
            cite = fetch_cite.fetcher.cn_doi(doi, code)
            click.echo(cite)
        except fetch_cite.fetcher.FormatNotSupportedError as exc:
            click.echo(exc.message, err=True)


if(__name__ == "__main__"):
    get_cite()
