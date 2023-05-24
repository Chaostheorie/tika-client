import magic

from tests.conftest import SAMPLE_DIR
from tika_client.client import TikaClient


class TestMetadataResource:
    def test_r_metadata_from_docx(self, tika_client: TikaClient):
        test_file = SAMPLE_DIR / "sample.docx"
        resp = tika_client.rmeta.html.parse(test_file, magic.from_file(str(test_file), mime=True))

        assert len(resp.documents) == 1

        document = resp.documents[0]

        assert document.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        assert "<body><p>This is an DOCX test document, also made September 14, 2022</p>\n</body>" in document.content
        assert document.created is None

    def test_r_metadata_from_docx_plain(self, tika_client: TikaClient):
        test_file = SAMPLE_DIR / "sample.docx"
        resp = tika_client.rmeta.plain.parse(test_file, magic.from_file(str(test_file), mime=True))

        assert len(resp.documents) == 1

        document = resp.documents[0]

        assert document.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        assert "This is an DOCX test document, also made September 14, 2022" in document.content
        assert document.created is None

    def test_r_meta_microsoft_word_docx(self, tika_client: TikaClient):
        test_file = SAMPLE_DIR / "microsoft-sample.docx"
        resp = tika_client.rmeta.html.parse(test_file, magic.from_file(str(test_file), mime=True))

        assert len(resp.documents) == 1

        document = resp.documents[0]

        assert document.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        assert (
            "<body><p>This is a sample document, generated by Microsoft Office on Wednesday, May 17, 2023.</p>\n<p>It is in English.</p>\n</body>"  # noqa: E501
            in document.content
        )
