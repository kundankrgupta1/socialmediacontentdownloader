import instaloader

loader = instaloader.Instaloader()

profile = instaloader.Profile.from_username(loader.context, 'mahi7781')

media = profile.mediacount
print("Total Post:", media)

igtv = profile.igtvcount
print("Total Reesl:",igtv)

private = profile.is_private
print("is account private:", private)

bio = profile.biography
print("Bio:",bio)

profile_pic = profile.profile_pic_url
print("Download Profile Picuter:", profile_pic)

business_type = profile.business_category_name
print("Account Type:", business_type)