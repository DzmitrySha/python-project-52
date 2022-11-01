# import pytest
#
#
# @pytest.mark.django_db
# @pytest.fixture
# def user_admin():
#     user_admin = User(username="admin2",
#                       first_name="Admin2",
#                       last_name="Petrovich2"
#                       )
#     user_admin.save()
#     return user_admin
#
#
# @pytest.mark.django_db
# def test_user(user_admin):
#     assert user_admin.id == 1
#     assert user_admin.username == "admin2"
#     assert user_admin.first_name == "Admin2"
#     assert user_admin.last_name == "Petrovich2"
#
