from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import (
    DiffViewerActionHook,
    HeaderActionHook,
    HeaderDropdownActionHook,
    ReviewRequestActionHook,
    ReviewRequestDropdownActionHook,
)
from reviewboard.reviews.actions import BaseReviewRequestAction


class TestExtensionAction(BaseReviewRequestAction):
    action_id = 'test-extension-action'
    label = 'Test Extension Action'



class ActionHooksExtension(Extension):
    def initialize(self):
        DiffViewerActionHook(self, actions=[
            {
                'id': 'diffviewer-action-hook',
                'label': 'DiffViewer Action Hook',
                'url': '#',
            }
        ])

        HeaderActionHook(self, actions=[
            {
                'id': 'header-action-hook',
                'label': 'Header Action Hook',
                'url': '#',
            },
        ])

        HeaderDropdownActionHook(self, actions=[
            {
                'label': 'Header Dropdown Action Hook',
                'items': [
                    {
                        'id': 'header-dropdown-action-hook-item-1',
                        'label': 'Header Item 1',
                        'url': '#',
                    },
                    {
                        'id': 'header-dropdown-action-hook-item-2',
                        'label': 'Header Item 2',
                        'url': '#',
                    },
                ],
            }
        ])

        ReviewRequestActionHook(self, actions=[
            {
                'label': 'Review Request Action Hook',
                'id': 'review-request-action-hook',
                'url': '#',
            },
        ])

        ReviewRequestDropdownActionHook(self, actions=[
            {
                'label': 'Review Request Dropdown Action Hook',
                'items': [
                    {
                        'id': 'review-request-dropdown-action-hook-item-1',
                        'label': 'Review Request Dropdown Item 1',
                        'url': '#',
                    },
                    {
                        'id': 'review-request-dropdown-action-hook-item-2',
                        'label': 'Review Request Dropdown Item 2',
                        'url': '#',
                    },
                ],
            },
        ])

        ReviewRequestActionHook(self, actions=[
            TestExtensionAction(),
        ])
