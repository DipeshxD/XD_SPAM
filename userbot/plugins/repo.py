@bot.on(admin_cmd(pattern="repo"))
@bot.on(sudo_cmd(pattern="repo", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    Repo = f"[Click Here](https://github.com/xdipesh/XD_SPAM-DEPLOY)"
    Deploy = f"[Click Here](https://heroku.com/deploy?template=https://github.com/xdipesh/XD_SPAM-DEPLOY)"
    await edit_or_reply(
        event, f"**XD_SPAM:** {Repo}\n\n**Deploy Now:** {Deploy}"
    )
