from statement_analyser.core.logging_config import configure_logging
from statement_analyser.core.config import settings

logger = configure_logging(__name__)

logger.info(f"Settings: {settings}")
