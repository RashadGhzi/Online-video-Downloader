
$('#url').click(function () {
    let csrftoken = $("input[name='csrfmiddlewaretoken']").val();
    let url = $("#link").val();
    console.log(url)
    data = { 'url': url, 'csrfmiddlewaretoken': csrftoken };
    $.ajax({
        type: 'POST',
        url: '/youtube/',
        data: data,
        success: (function (response) {
            // console.log(response);
            $("#vid-item").removeClass("d-none");

            $("#vid_thumbnail").html(`<div class="row vid-thumb bg-light rounded-2 p-4"><div class="col-sm-5"><div class="thumb-img rounded-2" style= "background-image: url('${response.vid_thumbnail}');"></div></div><div class="col-sm-6 mt-2"><div class="thumb-title">${response.vid_title}</div><div class="small mt-2">Duration : ${response.duration_formatted}</div></div</div>`);

            $("#vid_thumbnail").addClass("mb-2");

            $("#vid_brand").html(`<div class="bg-light py-2 text-dark rounded-2"><div class="py-2 d-flex justify-content-center align-items-center fw-bold"><b class='mx-4 thumb-logo'><i class="fab fa-youtube fa-3x youtube"></i></b>YouTube</div></div>`);

            vid_qual = response.quality
            let html = ''
            for (let i = 0; i < vid_qual.length; i++) {
                // const element = response.quality[i];

                html += `<div class="d-flex justify-content-center align-items-center mt-1 fm-1 f-size bg-light py-3 text-dark rounded-2"><div class="mx-auto fw-bold">${vid_qual[i]}.mp4</div><button type="button" class="mx-auto fw-bold btn btn-warning small" data-sid="${i}">Download</button></div>`

            }
            $("#vid_resolution").html(html)
        })
    })
})


$("#vid_resolution").on("click", "button", function () {
    let data_id = $(this).attr("data-sid");
    // console.log(data_id);
    data = { 'id': data_id }
    $.ajax({
        url: "/download/",
        method: "GET",
        data: data,
        success: function (response) {
            console.log(response);
        }
    })
})