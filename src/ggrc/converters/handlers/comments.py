# Copyright (C) 2019 Google Inc.
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>

"""Handlers comment entries."""

import datetime

from ggrc import db

from ggrc.converters import errors
from ggrc.converters.handlers.handlers import ColumnHandler
from ggrc.models import all_models
from ggrc.login import get_current_user_id, get_current_user


class CommentColumnHandler(ColumnHandler):
  """ Handler for comments """

  COMMENTS_SEPARATOR = ";;"

  @staticmethod
  def split_comments(raw_value):
    """Split comments"""
    res = [comment.strip() for comment in
           raw_value.rsplit(CommentColumnHandler.COMMENTS_SEPARATOR)
           if comment.strip()]
    return res

  def parse_item(self):
    """Parse a list of comments to be mapped.

    Parse a COMMENTS_SEPARATOR separated list of comments

    Returns:
      list of comments
    """
    comments = self.split_comments(self.raw_value)
    if self.raw_value and not comments:
      self.add_warning(errors.WRONG_VALUE,
                       column_name=self.display_name)
    return comments

  def get_value(self):
    return ""

  def set_obj_attr(self):
    """ Create comments """
    if self.dry_run or not self.value:
      return
    current_obj = self.row_converter.obj
    for description in self.value:
      if current_obj.access_control_list:
        current_user = get_current_user()
        assignee_types = [acl.ac_role.name
                          for person, acl in current_obj.access_control_list
                          if person == current_user]
        assignee_type = ','.join(assignee_types)
        comment = all_models.Comment(description=description,
                                     modified_by_id=get_current_user_id(),
                                     assignee_type=assignee_type)
      else:
        comment = all_models.Comment(description=description,
                                     modified_by_id=get_current_user_id())

      db.session.add(comment)
      mapping = all_models.Relationship(source=current_obj,
                                        destination=comment)
      db.session.add(mapping)

      notif_type_id = all_models.NotificationType.query.filter_by(
        name="comment_created").one().id
      notification = all_models.Notification(
        object=comment,
        send_on=datetime.datetime.utcnow(),
        notification_type_id=notif_type_id,
      )
      db.session.add(notification)
      self.row_converter.comments.append(comment)
