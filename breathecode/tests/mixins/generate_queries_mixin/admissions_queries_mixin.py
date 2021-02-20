"""
Collections of mixins used to login in authorize microservice
"""

class AdmissionsQueriesMixin():
    def generate_admissions_queries(self, **kwargs):
        """Generate queries"""
        return {
            'module': 'admissions',
            'models': ['Country', 'City', 'Academy', 'Certificate',
                'AcademyCertificate', 'Syllabus', 'Cohort', 'CohortUser']
        }
