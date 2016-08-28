import requests


class FormatNotSupportedError(Exception):
    pass


class FetchDOI_CN:
    """
    Class to handle getting citation data by DOI content negotiation
    """
    _format_codes = {
        'bibtex': 'application/x-bibtex',
        'citeproc': 'application/vnd.citationstyles.csl+json'
    }

    def get_supported_formats(self):
        """
        Return list of supported formats
        """
        return self._format_codes.keys()

    def fetch(self, doi, fmt):
        """
        Return citation in given format if content negotiation with said format
        is supported.
        """
        try:
            fmt_code = self._format_codes[fmt]
        except KeyError:
            raise FormatNotSupportedError(
                "Code for specifying format [{}] not known, could not complete"
                "request.".format(fmt)
            )
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
