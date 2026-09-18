"""Attach assembly videos and reference galleries to module tutorial pages."""

from __future__ import annotations

from html import escape

from docutils import nodes
from sphinx.application import Sphinx


VIDEOS = {
    "build/assembly-tutorials/modules/mod-frm-assembly": {
        "title": "Frame and enclosure assembly",
        "embed_url": "https://www.youtube-nocookie.com/embed/HBbVKG4gRxM",
        "watch_url": "https://youtu.be/HBbVKG4gRxM",
    },
    "build/assembly-tutorials/modules/mod-bmt-assembly": {
        "title": "Water bottle mount assembly",
        "embed_url": "https://www.youtube-nocookie.com/embed/RXxm7rT6lU0",
        "watch_url": "https://youtu.be/RXxm7rT6lU0",
    },
    "build/assembly-tutorials/modules/mod-fdr-aseembly": {
        "title": "Feeder module assembly",
        "embed_url": "https://www.youtube-nocookie.com/embed/1d9mzp3T70M",
        "watch_url": "https://youtu.be/1d9mzp3T70M",
    },
    "build/assembly-tutorials/modules/mod-lgt": {
        "title": "Light ring module assembly",
        "embed_url": "https://www.youtube-nocookie.com/embed/wTm9mv17IuQ",
        "watch_url": "https://youtu.be/wTm9mv17IuQ",
    },
    "build/assembly-tutorials/modules/mod-pbg-assembly": {
        "title": "Photobeam gate assembly",
        "embed_url": "https://www.youtube-nocookie.com/embed/AdGC6oDXmxQ",
        "watch_url": "https://youtu.be/AdGC6oDXmxQ",
    },
    "build/assembly-tutorials/modules/mod-scr-assembly": {
        "title": "Screen module assembly",
        "embed_url": "https://www.youtube-nocookie.com/embed/XW58EGUCWNA",
        "watch_url": "https://youtu.be/XW58EGUCWNA",
    },
}


GALLERIES = {
    "build/assembly-tutorials/modules/mod-frm-assembly": [
        ("/images/BB_V3_Material.jpg", "Open-BEATBox V3 parts prepared for assembly", "V3 parts and materials"),
        ("/images/real-build-setup.jpg", "Open-BEATBox enclosure during assembly", "Enclosure assembly"),
        ("/images/BB_Full-1.jpg", "Completed Open-BEATBox viewed from the front", "Completed enclosure — front"),
        ("/images/BB_Full-2.jpg", "Completed Open-BEATBox viewed from the side", "Completed enclosure — side"),
    ],
    "build/assembly-tutorials/modules/mod-bmt-assembly": [
        ("/images/BB-TIPS_Using-forceps-to-help-inserts.jpg", "Using forceps to position a threaded insert", "Positioning threaded inserts"),
        ("/images/BB_water-holder.jpg", "Completed Open-BEATBox water bottle holder", "Completed water bottle mount"),
    ],
    "build/assembly-tutorials/modules/mod-fdr-aseembly": [
        ("/videos/building_gifs/BB_Feeder_material.tiny.mp4", "Feeder parts laid out before assembly", "Prepare the feeder parts"),
        ("/images/Feeder/BB_Feeder-1.jpg", "First stage of the feeder housing assembly", "Prepare the housing — 1"),
        ("/images/Feeder/BB_Feeder-2.jpg", "Second stage of the feeder housing assembly", "Prepare the housing — 2"),
        ("/images/Feeder/BB_Feeder_IR-1.jpg", "First stage of feeder IR board installation", "Install the IR board — 1"),
        ("/images/Feeder/BB_Feeder_IR-2.jpg", "Second stage of feeder IR board installation", "Install the IR board — 2"),
        ("/images/Feeder/BB_Feeder_IR-3.jpg", "Third stage of feeder IR board installation", "Install the IR board — 3"),
        ("/images/Feeder/BB_Feeder_IR-4.jpg", "Fourth stage of feeder IR board installation", "Install the IR board — 4"),
        ("/images/Feeder/BB_Feeder_IR-5.jpg", "Fifth stage of feeder IR board installation", "Install the IR board — 5"),
        ("/images/Feeder/BB_Feeder_cable.jpg", "Feeder cable routed through the housing", "Route the IR cable"),
        ("/videos/building_gifs/BB_Feeder-motor.tiny.mp4", "Feeder stepper motor installation", "Install the stepper motor"),
        ("/images/Feeder/BB_Feeder_PCB_color-code.jpg", "Feeder PCB terminal wire color reference", "Connect the motor wires"),
        ("/videos/building_gifs/BB_Feeder-Assembly-motor-cables-to-PCB.tiny.mp4", "Connecting the feeder motor cables to the PCB", "Wire the motor to the PCB"),
        ("/images/Feeder.jpg", "Completed Open-BEATBox feeder viewed from the front", "Completed feeder — front"),
        ("/images/Feeder_side.jpg", "Completed Open-BEATBox feeder viewed from the side", "Completed feeder — side"),
    ],
    "build/assembly-tutorials/modules/mod-lgt": [
        ("/images/Light_bottom.jpg", "Bottom face of the assembled Open-BEATBox light ring", "PCB, housing, and connector"),
        ("/images/Light_top.jpg", "Top face of the assembled Open-BEATBox light ring", "Completed light ring and diffuser"),
    ],
    "build/assembly-tutorials/modules/mod-pbg-assembly": [
        ("/images/Tunnel-Passage-Corridor/BB_Tunnel_PCB.jpg", "Photobeam gate controller and IR circuit boards", "Prepare the electronics"),
        ("/images/Tunnel-Passage-Corridor/BB_Tunnel_IR-PCG-with-cables.jpg", "Photobeam gate IR boards connected with cables", "Connect the IR boards"),
        ("/images/Tunnel-Passage-Corridor/BB_Tunnel_PCG-assembly.jpg", "Circuit boards being installed in the photobeam passage", "Install and route the electronics"),
        ("/images/Tunnel-Passage-Corridor/BB_Tunnel_PCG-assembled.jpg", "Assembled photobeam gate electronics", "Check the assembled electronics"),
        ("/images/Tunnel.jpg", "Completed Open-BEATBox photobeam gate", "Completed photobeam gate"),
    ],
    "build/assembly-tutorials/modules/mod-scr-assembly": [
        ("/images/Screens/BB_Screen-1.jpg", "First stage of Open-BEATBox screen module assembly", "Screen assembly — 1"),
        ("/images/Screens/BB_Screen-2.jpg", "Second stage of Open-BEATBox screen module assembly", "Screen assembly — 2"),
        ("/images/Screens/BB_Screen-3.jpg", "Third stage of Open-BEATBox screen module assembly", "Screen assembly — 3"),
        ("/images/Screens/BB_Screen-4.jpg", "Fourth stage of Open-BEATBox screen module assembly", "Screen assembly — 4"),
        ("/images/Screens/BB_Screen-5.jpg", "Fifth stage of Open-BEATBox screen module assembly", "Screen assembly — 5"),
        ("/images/Screens/BB_Screen-6.jpg", "Sixth stage of Open-BEATBox screen module assembly", "Screen assembly — 6"),
        ("/images/Screens/BB_Screen_inside.jpg", "Interior of the Open-BEATBox screen module", "Interior layout"),
        ("/images/Screens/BB_Screen_long-cables.jpg", "Long cables routed inside the Open-BEATBox screen module", "Cable routing"),
        ("/images/Screens/BB_Screens-inside-view.jpg", "First inside view of the assembled screen module", "Inside view — 1"),
        ("/images/Screens/BB_Screens_Inside-view-2.jpg", "Second inside view of the assembled screen module", "Inside view — 2"),
        ("/images/electronics/photo-circuit-ecrans1.jpg", "First screen electronics connection reference", "Screen electronics — 1"),
        ("/images/electronics/photo-circuit-ecrans2.jpg", "Second screen electronics connection reference", "Screen electronics — 2"),
    ],
}


def _append_video(app: Sphinx, doctree: nodes.document, docname: str) -> None:
    video = VIDEOS.get(docname)
    if video is None or app.builder.format != "html":
        return

    title = str(video["title"])
    embed_url = str(video["embed_url"])
    watch_url = str(video["watch_url"])

    section = nodes.section(ids=["assembly-video-tutorial"])
    section += nodes.title(text="Assembly video")
    section += nodes.paragraph(
        text=(
            "Use this short visual walkthrough alongside the written instructions. "
            "The parts list, cautions, and checkpoints in this page remain essential."
        )
    )
    section += nodes.raw(
        "",
        (
            '<div class="assembly-video">'
            f'<iframe src="{escape(embed_url, quote=True)}" '
            f'title="{escape(title, quote=True)}" '
            'loading="lazy" '
            'allow="accelerometer; autoplay; clipboard-write; encrypted-media; '
            'gyroscope; picture-in-picture; web-share" allowfullscreen '
            'referrerpolicy="strict-origin-when-cross-origin"></iframe>'
            "</div>"
        ),
        format="html",
    )

    fallback = nodes.paragraph()
    fallback += nodes.Text("Player unavailable? ")
    fallback += nodes.reference(
        "",
        "Watch this tutorial on YouTube",
        refuri=watch_url,
        internal=False,
    )
    fallback += nodes.Text(".")
    section += fallback

    doctree += section


def _append_gallery(app: Sphinx, doctree: nodes.document, docname: str) -> None:
    gallery = GALLERIES.get(docname)
    if gallery is None or app.builder.format != "html":
        return

    section = nodes.section(ids=["assembly-gallery"])
    section += nodes.title(text="Assembly gallery")
    section += nodes.paragraph(
        text=(
            "Use these reference images alongside the numbered instructions above. "
            "They are ordered to follow the main stages of the assembly. Select an "
            "image to open the full-size version."
        )
    )

    figures = []
    for image_url, alt_text, caption in gallery:
        escaped_url = escape(image_url, quote=True)
        escaped_alt = escape(alt_text, quote=True)
        if image_url.lower().endswith((".mp4", ".webm", ".mov")):
            # Assembly clips are MP4 rather than animated GIF; autoplay them
            # muted and looping so they read the same way on the page.
            poster = escape(image_url.rsplit(".", 1)[0] + ".jpg", quote=True)
            media = (
                f'<video src="{escaped_url}" poster="{poster}" '
                'autoplay loop muted playsinline preload="metadata" '
                f'aria-label="{escaped_alt}"></video>'
            )
        else:
            media = f'<img src="{escaped_url}" alt="{escaped_alt}" loading="lazy">'
        figures.append(
            '<figure class="assembly-gallery-item">'
            f'<a href="{escaped_url}" target="_blank" rel="noopener noreferrer">'
            f"{media}"
            "</a>"
            f"<figcaption>{escape(caption)}</figcaption>"
            "</figure>"
        )

    section += nodes.raw(
        "",
        '<div class="assembly-gallery">' + "".join(figures) + "</div>",
        format="html",
    )
    doctree += section


def setup(app: Sphinx) -> dict[str, object]:
    app.connect("doctree-resolved", _append_video)
    app.connect("doctree-resolved", _append_gallery)
    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
