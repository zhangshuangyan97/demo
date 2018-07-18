from django.shortcuts import redirect


def login_required(view):
    def check(request):
        uid = request.session.get('uid')
        if uid is None:
            return redirect('/user/login/')
        else:
            return view(request)
    return check