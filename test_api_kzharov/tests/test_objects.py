import allure
from endpoints.get_object import GetObject


def test_get_obj_by_id(get_object_endpoint, new_obj):
    get_object_endpoint.get_by_id(new_obj)
    get_object_endpoint.check_response_is_200()
    get_object_endpoint.check_object_id(new_obj)


def test_post_obj(create_post_endpoint, payload, headers):
    create_post_endpoint.new_object(payload=payload, headers=headers)
    create_post_endpoint.check_response_title_is_correct(payload)
    create_post_endpoint.check_response_is_200()


def test_put_obj(put_object_endpoint, updated_payload, new_obj):
    put_object_endpoint.put_by_id(obj_id=new_obj, updated_payload=updated_payload)
    put_object_endpoint.check_response_title_is_correct(updated_payload)


def test_patch_obj(patch_object_endpoint, patch_payload, new_obj):
    patch_object_endpoint.patch_by_id(obj_id=new_obj, patch_payload=patch_payload)
    patch_object_endpoint.check_response_title_is_correct(patch_payload)


def test_delete_obj(delete_object_endpoint, new_obj):
    delete_object_endpoint.delete_by_id(obj_id=new_obj)
    delete_object_endpoint.check_response_is_200()
    get_object_endpoint = GetObject()
    get_object_endpoint.get_by_id(new_obj)
    get_object_endpoint.check_response_is_404()
