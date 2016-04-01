from iterable.run import make_request


def test_make_request():
    """Tests that make_request returns 200 on successful request"""
    assert 200 == make_request('http://iterable.io')


def test_make_request_fail():
    """Test that make_request doesn't return 200 on failed request"""
    assert 200 != make_request('http://iterable.io/wtf')
