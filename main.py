import logging

def establish_session(user_id):
  logging.info("Establishing session for user: {}".format(user_id))

  user = f"find_user{user_id}"

  if not user:
    logging.error("Unable to find user {}!".format(user_id))
    raise f"UserNotFoundException{user}"

  logging.login_user(user)

  logging.info("Established session for user: {}".format(user_id))
  logging.debug("Last logged in: {}".format(user.last_login_time))

  return user