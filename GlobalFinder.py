from SublimeLinter.lint import Linter


class GlobalFinder(Linter):
	cmd = 'luacheck - --formatter=plain --std none --only [111,112,113] --no-unused --no-redefined --no-unused-args --no-unused-secondaries --no-self --no-max-line-length --no-max-code-line-length --no-max-string-line-length --no-max-comment-line-length --codes --ranges --filename @'
	regex = (
		r'^.+:(?P<line>\d+):(?P<col>\d+)\-(?P<col_end>\d+): '
		r'\((?:(?P<error>E\d+)|(?P<warning>W\d+))\) '
		r'(?P<message>.+)'
	)
	defaults = {
		'selector': 'source.lua - meta.tag.xml, source.lua.wow - meta.tag.xml, source.luae'
	}

	def split_match(self, match):
		match, line, col, error, warning, msg, near = super().split_match(match)
		col_end = int(match.group(3))
		token_len = col_end - col
		return match, line, col, error, warning, msg, "." * token_len
