@login_required
def dashboard(request):
    zipcode = request.GET.get('zip_code')
    if zipcode:
        profiles = Profile.objects.filter(is_teacher=True, zip_code=zipcode)
        zcdb = ZipCodeDatabase()
        zipcode_derived = zcdb[zipcode]
        lng = zipcode_derived.longitude
        lat = zipcode_derived.latitude
        radius = 10
        point = Point(lng, lat) 
        Profile.objects.filter(is_teacher=True, location__distance_lt=(point, Distance(km=radius)))
    else:   
        profiles = Profile.objects.filter(is_teacher=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(profiles, 10)
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        profiles = paginator.page(1)
    except EmptyPage:
        profiles = paginator.page(paginator.num_pages)
    context = {
        'profiles': profiles
    }
    return render(request,
                  'account/dashboard.html',context
                  )	