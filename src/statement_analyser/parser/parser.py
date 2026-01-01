from statement_analyser.core.logging_config import configure_logging
from typing import Optional
import pymupdf.layout
import pymupdf4llm
from statement_analyser.core.config import settings

logger = configure_logging(__name__)


def parse_pdf_to_markdown(pdf_path: str, password: Optional[str] = None):
    logger.info(f"Parsing PDF: {pdf_path}")
    doc = pymupdf.open(pdf_path)
    if doc.needs_pass > 0:
        if password is not None:
            logger.info(
                "Document needs password. Attempting to authenticate with the given password"
            )
            try:
                doc.authenticate(password)
                if not doc.is_encrypted:
                    logger.info("Password is correct. Parsing to markdown")
                else:
                    logger.error(
                        "Provided password is incorrect. Please provide the correct password."
                    )
                    raise ValueError(
                        "Provided password is incorrect. Please provide the correct password."
                    )

            except Exception as e:
                logger.error(f"Failed to authenticate with password: {e}")
                raise e

        else:
            raise ValueError("Document needs password. Please provide a password.")
    md = pymupdf4llm.to_markdown(doc)
    return md


if __name__ == "__main__":
    pdf_path = settings.project_root / "data" / "Account_stmt.pdf"
    md = parse_pdf_to_markdown(pdf_path=pdf_path)
    print(md)
