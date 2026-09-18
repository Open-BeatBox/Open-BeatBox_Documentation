# Video tutorials

Six short 720p tutorials complement the written module guides. All six are published on the project's YouTube channel and embedded directly in their matching Sphinx pages. The written guides remain essential because they contain the full parts lists, cautions, checkpoints, and revision information.

## Watch the tutorials

The project's YouTube channel is live at <https://www.youtube.com/@open-beatbox/>, and every assembly tutorial is public. Each video is also embedded at the bottom of its written guide, so you can follow the numbered steps and the walkthrough side by side.

| Tutorial | Written guide | Public video |
| --- | --- | --- |
| Frame and enclosure | {doc}`Open guide with video <assembly-tutorials/modules/mod-frm-assembly>` | [Watch on YouTube](https://youtu.be/HBbVKG4gRxM) |
| Water bottle mount | {doc}`Open guide with video <assembly-tutorials/modules/mod-bmt-assembly>` | [Watch on YouTube](https://youtu.be/RXxm7rT6lU0) |
| Feeder module | {doc}`Open guide with video <assembly-tutorials/modules/mod-fdr-aseembly>` | [Watch on YouTube](https://youtu.be/1d9mzp3T70M) |
| Light ring | {doc}`Open guide with video <assembly-tutorials/modules/mod-lgt>` | [Watch on YouTube](https://youtu.be/wTm9mv17IuQ) |
| Photobeam gate | {doc}`Open guide with video <assembly-tutorials/modules/mod-pbg-assembly>` | [Watch on YouTube](https://youtu.be/AdGC6oDXmxQ) |
| Screen module | {doc}`Open guide with video <assembly-tutorials/modules/mod-scr-assembly>` | [Watch on YouTube](https://youtu.be/XW58EGUCWNA) |

[Open the Open-BEATBox YouTube channel](https://www.youtube.com/@open-beatbox/).

## Maintenance notes

- Keep the 720p MP4 originals as archival assets outside the Git repository.
- Use the naming convention in the [assembly documentation conventions](https://github.com/Open-BeatBox/assembly-tutorials/blob/main/conventions.md).
- Captions or a transcript are still to be added to each video; thumbnails and descriptions are in place.
- The `embed_url` and `watch_url` values are held in `docs/source/_ext/assembly_videos.py`; update them there and in the table above if a video is ever re-uploaded.
- Verify playback on desktop and mobile after any re-upload.

Large MP4 files should not be committed directly to the website repository; YouTube carries the website experience. A Zenodo deposit for the archival copies is planned but deferred: it waits on the outstanding hardware and software elements, and the DOI is currently targeted at the journal submission rather than the BioRxiv preprint.
