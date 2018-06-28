import click
import fetch_cite.fetcher


@click.command()
@click.argument('dois', nargs=-1)
@click.option('--fmt', nargs=1, default='bibtex',
              help='Format to provide citation information in,'
              'defaults to bibtex')
@click.pass_context
def fetch(ctx, dois, fmt):
    """Fetch citations for DOIs in FMT format"""
    fc = fetch_cite.fetcher.FetchDOI_CN()
    if fmt not in fc.get_supported_formats():
        click.echo("Format [{}] not supported".format(fmt))
        return
    for doi in dois:
        try:
            cite = fc.fetch(doi, fmt)
            click.echo(cite)
        except fetch_cite.fetcher.FormatNotSupportedError as exc:
            click.echo(str(exc), err=True)


if(__name__ == "__main__"):
    fetch()
