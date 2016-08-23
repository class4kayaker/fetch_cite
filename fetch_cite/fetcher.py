import requests

_format_codes = {
    'bibtex': 'application/x-bibtex'
}


class FormatNotSupportedError(Exception):
    pass


def get_format_code(name):
    return _format_codes[name]


def cn_doi(doi, fmt_code):
    """
    Return citation in given format if content negotiation is supported for
    said format.
    """
    url = "http://dx.doi.org/"+doi
    headers = {"Accept": fmt_code}
    r = requests.get(url, headers=headers)

    if not r.status_code == requests.codes.ok:
        raise FormatNotSupportedError(
            "Format [{}] not available for doi {} by content "
            "negotiation".format(fmt_code, doi)
        )

    if not r.headers['content-type'] == fmt_code:
        raise FormatNotSupportedError(
            "Format [{}] not available for doi {} by content "
            "negotiation, got {}".format(fmt_code,
                                         doi,
                                         r.headers['content-type'])
        )

    return r.text
