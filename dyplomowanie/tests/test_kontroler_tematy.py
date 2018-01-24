# from django.test import TestCase
#
# from dyplomowanie.DTO.tematy import TematDTO
# from dyplomowanie.kontroler.tematy import Topics
# from dyplomowanie.model.Temat import Temat
#
#
# class Test1(TestCase):
#
#     def test_create_DTO_list_empty(self):
#
#         controler = Topics()
#         _input = []
#         expected = []
#
#         result = controler.create_DTO_list(_input)
#
#         self.assertEqual(result, expected)
#
#
#     def test_create_DTO_list_one_object(self):
#         controler = Topics()
#
#         t = Temat(
#             trescpl='tresc',
#             tresceng='content',
#             nauczycielakademickiid_id=1,
#             typ_id=1,
#             jezykrealizacji_id=1,
#             czyzatwierdzony=True,
#             czywolny=True
#         )
#
#         _input = [t]
#         expected = [TematDTO(t.id, t.trescpl, t.nauczycielakademickiid, 'wolny')]
#
#         result = controler.create_DTO_list(_input)
#
#         self.assertEqual(result, expected)