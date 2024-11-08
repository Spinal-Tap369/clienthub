from django.shortcuts import redirect

def get_redirect_url_for_user(user):
    if user.groups.filter(name="Client Group").exists():
        return redirect('client_homepage')
    elif user.groups.filter(name="Support Group").exists():
        return redirect('support_homepage')
    else:
        return redirect('default_homepage')
