import requests
import inspect
import json

class LoginException(Exception):
	pass

class PTHAPI:
	def __init__(self, username, password):
		self.api_url = "https://passtheheadphones.me/ajax.php"

		self.session = requests.Session()

		self.headers = {
			'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
		}

		self.username = username
		self.password = password

		self._login()

	def _login(self):
		login_page = "https://passtheheadphones.me/login.php"

		data = {'username': self.username,
						'password': self.password,
						'keeplogged': 1 }

		r = self.session.post(login_page, data=data)

		if r.status_code != 200:
			raise LoginException

	def _request(self, action, arguments):
		arg_string = "?action=%s" % action

		for key, value in arguments.items():
			arg_string += "&%s=%s" % (key, str(value))

		url = self.api_url + arg_string

		r = self.session.get(url)

		return json.loads(r.text)

	def index(self):
		response = self._request("index", arguments=None)
		
		return response

	def user_by_id(self, user_id):
		arguments = { "id": user_id }
		response = self._request("user", arguments)
		
		return response

	def user_by_name(self, search_str, page):
		arguments = { 'search': search_str,
									'page': page }
		response = self._request("usersearch", arguments)

		return response

	def user_inbox(self, page_number="", type="", sort="", filter_str="", search_type=""):
		arguments = { "page": page_number,
									"type": type,
									"sort": sort,
									"search": filter_str,
									"searchtype": search_type
								}
		response = self._request("inbox", arguments)

		return response

	def view_conversation(self, message_id):
		arguments = { "type": "viewconv",
									"id": message_id }

		response = self._request("inbox", arguments) 

		return response

	def top_10(self, type="torrents", limit=10):
		arguments = { "type": type,
									"limit": limit }

		response = self._request("top10", arguments)

		return response

	def request_search(self, search_str, page, tag, tags_type, show_filled):
		arguments = { 'search': search_str,
									'page': page,
									'tag': tag,
									'tags_type': tags_type,
									'shwo_filled': show_filled }
		response = self._request("requests", arguments)

		return response

	def torrent_search(self, search_str, page, taglist="", tags_type="", order_by="",
										 order_way="", filter_cat="", freetorrent="", vanityhouse="",
										 scene="", haslog="", releasetype="", media="", format="",
										 encoding="", artistname="", filelist="", groupname="",
										 recordlabel="", cataloguenumber="", year="", remastertitle="",
										 remasteryear="", remaster_record_label="", remastercataloguenumber=""):
	
		frame = inspect.currentframe()

		args, _, _, values = inspect.getargvalues(frame)

		arguments = dict()

		for arg in args:
			arguments[arg] = values[arg]

		del(arguments["self"])

		print(arguments)

		response = self._request("browse", arguments)

		return response

	def user_bookmarks(self, type):
		arguments = { 'type': type }

		response = self._request("bookmarks", arguments)

		return response

	def user_subscriptions(self, show_unread):
		arguments = { 'showunread': show_unread }

		response = self._request("subscriptions", arguments)

		return response

	def forum_view(self, forum_id, page):
		arguments = { 'type': "viewforum",
									'forumid': forum_id,
									'page': page }

		response = self._request("forum", arguments)

		return response

	def thread_view(self, thread_id, page, updatelastread=0):
		arguments = { "type": 'viewthread',
									"threadid": thread_id,
									"page": page,
									"updatelastread": updatelastread }

		response = self._request("forum", arguments)

		return response

	def artist_search(self, artist_id="", artist_name=""):
		arguments = { 'id': artist_id,
									'artistname': artist_name }

		response = self._request("artist", arguments)

		return response

	def torrent_by_id(self, torrent_id):
		arguments = { 'id': torrent_id }

		response = self._request("torrent", arguments)

		return response

	def torrent_group_by_id(self, group_id):
		arguments = { 'id': group_id }

		response = response = self._request("torrentgroup", arguments)

		return response

	def request_by_id(self, request_id, page):
		arguments = { 'id': request_id,
									'page': page}

		response = self._request("request", arguments)

		return response

	def collage_by_id(self, collage_id):
		arguments = { 'id': collage_id }

		response = self._request("collage", arguments)

		return response

	def user_notifications(self, page):
		arguments = { 'page': page }

		response = self._request("notifications", arguments)

		return response

	def similar_artists(self, artist_id, limit):
		arguments = { 'id': artist_id,
									'limit': limit }

		response = self._request("similar_artists", arguments)

		return response

	def announcements(self):
		response = self._request("announcements", arguments)

		return response

class PTHUser:
	pass

if __name__ == "__main__":
	pth = PTHAPI("srnty", "Rache171")
	pth.user_by_name("a", 1)
