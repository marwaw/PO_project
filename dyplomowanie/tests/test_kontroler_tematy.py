from unittest.mock import MagicMock

import pytest

from dyplomowanie.DTO.tematy import TematDTO
from dyplomowanie.kontroler.tematy import Topics


class TestTopics:
    @pytest.mark.parametrize("test_input,expected", [
        ([], []),  # działa dla pustej listy
        ([MagicMock(id=1,
                    trescpl='a',
                    nauczycielakademickiid='Jan Nowak',
                    czywolny=True)],
         [TematDTO(1, 'a', 'Jan Nowak', 'wolny')]),
        ([MagicMock(id=1,
                    trescpl='a',
                    nauczycielakademickiid='Jan Nowak',
                    czywolny=True),
          MagicMock(id=2,
                    trescpl='druga tresc',
                    nauczycielakademickiid='Jan Kowal',
                    czywolny=False)
          ],
         [TematDTO(1, 'a', 'Jan Nowak', 'wolny'),
          TematDTO(2, 'druga tresc', 'Jan Kowal', 'zajęty')]),
    ])
    def test_create_DTO_list(self, test_input, expected):
        t = Topics()
        assert t.create_DTO_list(test_input) == expected
