"""Axes behaviour."""


def lines(
    *,
    base_width=0.5,
    color="black",
    spines_left=True,
    spines_right=True,
    spines_top=True,
    spines_bottom=True,
    xtick_direction="inout",
    ytick_direction="inout",
    line_base_ratio=1.5,
    grid_alpha=0.25,
    grid_linestyle="solid",
):
    return {
        # Set the line-widths appropriately (including the grid)
        "axes.linewidth": base_width,
        "lines.linewidth": line_base_ratio * base_width,
        "xtick.major.width": base_width,
        "ytick.major.width": base_width,
        "xtick.minor.width": 0.5 * base_width,
        "ytick.minor.width": 0.5 * base_width,
        "xtick.major.size": 1.5 + 3 * base_width,
        "ytick.major.size": 1.5 + 3 * base_width,
        "xtick.minor.size": 1.0 + 3 * 0.5 * base_width,
        "ytick.minor.size": 1.0 + 3 * 0.5 * base_width,
        "grid.linewidth": base_width,
        # Legend
        "patch.linewidth": base_width,
        # Tick directions
        "xtick.direction": xtick_direction,
        "ytick.direction": ytick_direction,
        # Change the text color
        "text.color": color,
        "axes.edgecolor": color,
        "axes.labelcolor": color,
        "xtick.color": color,
        "ytick.color": color,
        "grid.color": color,
        "legend.edgecolor": "inherit",  # inherit color from axes. passing 'color' leads to awkward future warnings.
        # Update the linestyle of the grid
        # (it shares a color with the frame, and needs to be distinguishable)
        "grid.linestyle": grid_linestyle,
        "grid.alpha": grid_alpha,
        # Set visibility of spines
        "axes.spines.left": spines_left,
        "axes.spines.right": spines_right,
        "axes.spines.top": spines_top,
        "axes.spines.bottom": spines_bottom,
    }


def legend(*, shadow=False, frameon=True, fancybox=False):
    return {
        "legend.shadow": shadow,
        "legend.frameon": frameon,
        "legend.fancybox": fancybox,
    }


def face(*, color="none"):
    return {"axes.facecolor": color}
