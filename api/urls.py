from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('employees', EmployeesViewSet, 'employees')

router.register('average/age/industry', AverageAgePerIndustryViewSet, 'average-age-per-industry')
router.register('highest/age/industry', HighestAgePerIndustryViewSet, 'highest-age-per-industry')
router.register('lowest/age/industry', LowestAgePerIndustryViewSet, 'lowest-age-per-industry')

router.register('average/salaries/experience', AverageSalariesPerExperienceViewSet, 'average-salaries-per-experience')
router.register('highest/salaries/experience', HighestSalariesPerExperienceViewSet, 'highest-salaries-per-experience')
router.register('lowest/salaries/experience', LowestSalariesPerExperienceViewSet, 'lowest-salaries-per-experience')

router.register('average/salaries/industry', AverageSalariesPerIndustryViewSet, 'average-salaries-per-industry')
router.register('highest/salaries/industry', HighestSalariesPerIndustryViewSet, 'highest-salaries-per-industry')
router.register('lowest/salaries/industry', LowestSalariesPerIndustryViewSet, 'lowest-salaries-per-industry')

router.register('average/salaries/gender', AverageSalariesPerGenderViewSet, 'average-salaries-per-gender')
router.register('highest/salaries/gender', HighestSalariesPerGenderViewSet, 'highest-salaries-per-gender')
router.register('lowest/salaries/gender', LowestSalariesPerGenderViewSet, 'lowest-salaries-per-gender')

urlpatterns = router.urls
