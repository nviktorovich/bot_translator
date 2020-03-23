from .constant import Constant as CT


class UserOptions:
	options = {
		'id':
			(1, 2, 3, 4, 5, 6),
		'title':
			(CT.TITLE_RUS_ENG, CT.TITLE_RUS_ESP, CT.TITLE_ENG_RUS, CT.TITLE_ENG_ESP, CT.TITLE_ESP_ENG, CT.TITLE_ESP_RUS),
		'description':
			(CT.DSCRP_RUS_ENG, CT.DSCRP_RUS_ESP, CT.DSCRP_ENG_RUS, CT.DSCRP_ENG_ESP, CT.DSCRP_ESP_ENG, CT.DSCRP_ESP_RUS),
		'thumb_url':
			(CT.FLAG_ENG, CT.FLAG_ESP, CT.FLAG_RUS, CT.FLAG_ESP, CT.FLAG_ENG, CT.FLAG_RUS),
		'message_text':
			((CT.RUS, CT.ENG), (CT.RUS, CT.ESP), (CT.ENG, CT.RUS), (CT.ENG, CT.ESP), (CT.ESP, CT.ENG), (CT.ESP, CT.RUS))
	}