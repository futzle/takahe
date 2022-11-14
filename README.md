![takahē](static/img/logo-128.png)

A *very experimental* Fediverse server for microblogging/"toots". Not fully functional yet - I'm still working on making all the basic bits work!

Indended features:

* Can run on serverless hosting (no need for worker daemons)
* Multiple account domains possible per server
* Async evented core for fan-out/delivery
* Mastodon client API compatible (eventually)


## Deployment

### Requirements:

- **Python** 3.11
- **PostgreSQL** 14+
- **Lots of patience** This is *very experimental*

### Setup

More deployment docs will come soon! Just know that you need to run the Takahē
Django app, and then either hit `/.stator/runner/` or run `./manage.py runstator`
at least every 30 seconds.

## Roadmap

Takahē is still under very active development towards something I'm willing to
call a beta. I've grouped features here into milestones, along with if they're
done yet or not. None of this is final, and the further into the future it is,
the less sure I am about it.

### Alpha

- [x] Create posts
- [x] Receive posts
- [ ] Receive post deletions
- [x] Set content warnings on posts
- [ ] Show content warnings on posts
- [ ] Attach images to posts
- [ ] Receive images on posts
- [ ] Create boosts
- [x] Receive boosts
- [ ] Create likes
- [x] Receive likes
- [x] Create follows
- [x] Receive and accept follows
- [x] Receive follow undos
- [ ] Undo follows
- [x] Home timeline (posts and boosts from follows)
- [ ] Notifications page (followed, boosted, liked)
- [x] Local timeline
- [x] Federated timeline
- [x] Profile pages
- [ ] Settable icon and background image for profiles
- [ ] Following page
- [ ] Followers page
- [x] Multiple domain support
- [x] Multiple identity support
- [x] Serverless-friendly worker subsystem
- [ ] Settings subsystem
- [ ] Server management page
- [ ] Domain management page
- [ ] Email subsystem
- [ ] Signup flow
- [ ] Password change flow
- [ ] Password reset flow

### Beta

- [ ] Delete posts
- [ ] Emoji fetching and display
- [ ] Emoji creation
- [ ] Image descriptions
- [ ] Flag for moderation
- [ ] Moderation queue
- [ ] User management page
- [ ] Server defederation
- [ ] IP banning
- [ ] Trends subsystem and moderation
- [ ] Filters for posts/boosts
- [ ] Reply threading on post creation
- [ ] Display posts with reply threads
- [ ] Create polls on posts
- [ ] Receive polls on posts
- [ ] OAuth subsystem

### 1.0

- [ ] Server announcements
- [ ] Automated post deletion
- [ ] Post popularity system (for long gaps between timeline views)
- [ ] Mastodon client API

### Future

- [ ] Relays?
- [ ] Mastodon backup import? (would need url mapping for actors)

## Contributing

If you'd like to contribute, please read [CONTRIBUTING.md](./CONTRIBUTING.md).
