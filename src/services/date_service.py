import dateparser

from datetime import datetime
from typing import Any, Dict, Optional, Tuple

from django.db.models import Q
from django.utils import timezone


class DateService:
    def parse(
            self,
            date_string: Optional[str],
            settings: Optional[Dict[str, Any]] = None,
    ) -> Optional[datetime]:
        if not date_string:
            return None

        if settings is None:
            settings = {}

        return dateparser.parse(
            date_string,
            settings={
                'RETURN_AS_TIMEZONE_AWARE': True,
                'TIMEZONE': timezone.get_current_timezone_name(),
                **settings,
            }
        )

    def to_q(self, since: datetime, until: datetime) -> Q:
        since_filter = Q(
            created_at__gte=since
        ) if since else Q()
        until_filter = Q(
            created_at__lte=until
        ) if until else Q()

        return since_filter & until_filter

    def get_since_until(
            self,
            since: Optional[str],
            since_default: Optional[str],
            until: Optional[str],
            until_default: Optional[str],
    ) -> Tuple[datetime, datetime]:
        since_option = since if since else since_default
        until_option = until if until else until_default

        return self.parse(since_option), self.parse(until_option)
