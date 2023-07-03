"""Tests for the Site model."""

def test_create_site():
 """Check a site is created correctly given a name."""
    from catchment.models import Site
    name = 'PL23'
    p = Site(name=name)
    assert p.name == name
 
 def test_create_catchment():
    """Check a catchment is created correctly given a name."""
    from catchment.models import Catchment
    name = 'Spain'
    catchment = Catchment(name=name)
    assert catchment.name == name

def test_catchment_is_location():
    """Check if a catchment is a location."""
    from catchment.models import Catchment, Location
    catchment = Catchment("Spain")
    assert isinstance(catchment, Location)

def test_site_is_location():
     """Check if a site is a location."""
     from catchment.models import Site, Location
     PL23 = Site("PL23")
     assert isinstance(PL23, Location)

def test_sites_added_correctly():
    """Check sites are being added correctly by a catchment. """
    from catchment.models import Catchment, Site
    catchment = Catchment("Spain")
    PL23 = Site("PL23")
    catchment.add_site(PL23)
    assert catchment.sites is not None
    assert len(catchment.sites) == 1

def test_no_duplicate_sites():
    """Check adding the same site to the same catchment twice does not result in duplicates. """
    from catchment.models import Catchment, Site
    catchment = Catchment("Sheila Wheels")
    PL23 = Site("PL23")
    catchment.add_site(PL23)
    catchment.add_site(PL23)
    assert len(catchment.sites) == 1  