$(document).ready(function () {
    const interests = [
        "Archery",
        "Beekeeping",
        "Camping",
        "Computer Programming",
        "Darts",
        "Fashion",
        "Gaming",
        "Gongoozling",
        "Hiking",
        "Hydroponics",
        "Juggling",
        "Kayaking",
        "Lockpicking",
        "Magic",
        "Marbles",
        "Mountain Biking",
        "Mushroom Hunting",
        "Painting",
        "Parkour",
        "Rock Climbing",
        "Roller Derby",
        "Running",
        "Sailing",
        "Skiing",
        "Snowboarding",
        "Speedcubing",
        "Tai Chi",
        "Ultimate Disc",
        "Whittling",
        "Yoga"
    ];
    $(".autocomplete").autocomplete({
        source: interests
    });
});