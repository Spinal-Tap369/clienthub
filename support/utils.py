from django.core.exceptions import PermissionDenied
from functools import wraps
from django.shortcuts import redirect

def group_required(group_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Check if the user is authenticated
            if not request.user.is_authenticated:
                print("User not authenticated, redirecting to login.")
                return redirect('login_user')  # Redirect if not authenticated
            
            # Access user's profile, team, and group information
            user_profile = getattr(request.user, 'profile', None)
            if user_profile:
                print(f"User profile found: {user_profile}")
                user_team = user_profile.team
                if user_team:
                    print(f"User team found: {user_team}")
                    user_group = user_team.group
                    if user_group:
                        print(f"User group found: {user_group.name}")
                        if user_group.name == group_name:
                            return view_func(request, *args, **kwargs)  # Allow access if in the specified group
            
            # If any check fails, print what was missing and deny access
            print("Access denied: User not in the required group or group not found.")
            raise PermissionDenied  # 403 if not in the specified group
        return _wrapped_view
    return decorator
